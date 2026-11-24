import { motion } from 'framer-motion'
import { useInView } from 'framer-motion'
import { useRef } from 'react'
import { fadeSlideUp, fadeSlideLeft, staggerContainer } from '@/lib/motion'
import { Terminal, Code2, Palette } from 'lucide-react'

const HIGHLIGHTS = [
  {
    icon: <Terminal size={22} />,
    title: 'Programming',
    desc: 'Working with C, Java, Python, JavaScript, SQL, and data structures and algorithms.',
  },
  {
    icon: <Code2 size={22} />,
    title: 'AI & Web Projects',
    desc: 'Building AI-assisted products and web applications, including ClimateAI Maharashtra and CoffeeRide AI.',
  },
  {
    icon: <Palette size={22} />,
    title: 'UI/UX & Frontend',
    desc: 'Interested in creating polished, interactive user experiences and modern frontend interfaces.',
  },
]

export default function About() {
  const ref = useRef(null)
  const inView = useInView(ref as React.RefObject<Element>, { once: true, margin: '-80px' })

  return (
    <section id="about" className="relative z-10 section-padding">
      <div className="section-container">
        <div className="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
          <motion.div
            ref={ref}
            initial="hidden"
            animate={inView ? 'visible' : 'hidden'}
            variants={fadeSlideLeft}
          >
            <p className="section-label">About Me</p>
            <h2 className="section-heading mb-6">
              Building at the intersection of{' '}
              <span className="gradient-text italic">technology</span> and design.
            </h2>
            <div className="space-y-4 text-[var(--fg-muted)] leading-relaxed text-lg">
              <p>
                I'm a second-year Computer Engineering student at Fr. Conceicao Rodrigues Institute of Technology (FCRIT), interested in AI-powered products, frontend development, and user experience design.
              </p>
              <p>
                I work with C, Java, Python, SQL, and modern web technologies. My project work includes an international hackathon climate-intelligence prototype and a GenAI-powered location-analysis concept.
              </p>
              <p>
                I'm currently looking for remote internship opportunities where I can contribute to frontend, UI/UX, and AI product development while continuing to grow as an engineer.
              </p>
            </div>
          </motion.div>

          <motion.div
            initial="hidden"
            animate={inView ? 'visible' : 'hidden'}
            variants={staggerContainer}
            className="grid gap-4"
          >
            {HIGHLIGHTS.map((h) => (
              <motion.div
                key={h.title}
                variants={fadeSlideUp}
                className="glass-hover rounded-xl p-5 flex gap-4 items-start"
              >
                <div className="shrink-0 w-10 h-10 rounded-lg bg-[var(--node)]/10 flex items-center justify-center text-[var(--node)]">
                  {h.icon}
                </div>
                <div>
                  <h3 className="font-semibold text-[var(--fg)] mb-1">{h.title}</h3>
                  <p className="text-sm text-[var(--fg-muted)] leading-relaxed">{h.desc}</p>
                </div>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  )
}
