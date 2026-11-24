import { useState, useEffect, useRef } from 'react'
import { motion, useInView } from 'framer-motion'
import SectionTitle from '@/components/ui/SectionTitle'
import { fetchSkills } from '@/lib/api'
import { staggerContainer, fadeSlideUp } from '@/lib/motion'
import type { Skill } from '@/types'

const CATEGORY_META: Record<string, { label: string; color: string }> = {
  Languages: { label: 'Languages', color: 'var(--node)' },
  Backend: { label: 'Backend', color: 'var(--synapse)' },
  Frontend: { label: 'Frontend', color: '#f97316' },
  Design: { label: 'Design', color: '#a78bfa' },
  Tools: { label: 'Tools', color: '#a78bfa' },
  Core: { label: 'Core CS', color: 'var(--node)' },
}

function CategoryBlock({ category, skills }: { category: string; skills: Skill[] }) {
  const meta = CATEGORY_META[category] ?? { label: category, color: 'var(--node)' }
  return (
    <motion.div variants={fadeSlideUp} className="glass rounded-2xl p-6">
      <div className="flex items-center gap-2 mb-5">
        <div
          className="w-2.5 h-2.5 rounded-full"
          style={{ background: meta.color, boxShadow: `0 0 8px ${meta.color}` }}
          aria-hidden="true"
        />
        <h3 className="font-mono text-sm font-semibold text-[var(--fg)]">{meta.label}</h3>
      </div>
      <div className="flex flex-wrap gap-2">
        {skills.map((skill) => (
          <span key={skill.id} className="tag-pill">{skill.name}</span>
        ))}
      </div>
    </motion.div>
  )
}

export default function Skills() {
  const [skills, setSkills] = useState<Skill[]>([])
  const [loading, setLoading] = useState(true)
  const sectionRef = useRef<HTMLElement>(null)
  const inView = useInView(sectionRef, { once: true, margin: '-40px' })

  useEffect(() => {
    fetchSkills()
      .then(setSkills)
      .finally(() => setLoading(false))
  }, [])

  const grouped = skills.reduce<Record<string, Skill[]>>((acc, skill) => {
    ;(acc[skill.category] ??= []).push(skill)
    return acc
  }, {})

  return (
    <section ref={sectionRef} id="skills" className="relative z-10 section-padding">
      <div className="section-container">
        <SectionTitle label="// skills" title="What I work with" />
        {loading ? (
          <div className="flex justify-center py-16">
            <div className="w-8 h-8 rounded-full border-2 border-[var(--node)] border-t-transparent animate-spin" />
          </div>
        ) : (
          <motion.div
            initial="hidden"
            animate={inView ? 'visible' : 'hidden'}
            variants={staggerContainer}
            className="grid sm:grid-cols-2 xl:grid-cols-3 gap-5"
          >
            {Object.keys(CATEGORY_META).map((category) =>
              grouped[category] ? <CategoryBlock key={category} category={category} skills={grouped[category]} /> : null
            )}
          </motion.div>
        )}
      </div>
    </section>
  )
}
