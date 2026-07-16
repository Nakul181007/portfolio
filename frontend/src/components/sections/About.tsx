import { motion } from 'framer-motion'
import { useInView } from 'framer-motion'
import { useRef } from 'react'
import { fadeSlideUp, fadeSlideLeft, staggerContainer } from '@/lib/motion'
import { Terminal, Code2, Award } from 'lucide-react'

const HIGHLIGHTS = [
  {
    icon: <Terminal size={22} />,
    title: 'Languages & Core',
    desc: 'Expertise in C++, Java, and Python with a strong foundation in Data Structures and Algorithms.',
  },
  {
    icon: <Code2 size={22} />,
    title: 'Full-Stack Dev',
    desc: 'Building robust, modern web apps with React, Vite, FastAPI, and Spring Boot.',
  },
  {
    icon: <Award size={22} />,
    title: 'Placement & Leadership',
    desc: 'Secured top technical placements; mentored peers and coordinated preparation bootcamps.',
  },
]

export default function About() {
  const ref = useRef(null)
  const inView = useInView(ref as React.RefObject<Element>, { once: true, margin: '-80px' })

  return (
    <section id="about" className="relative z-10 section-padding">
      <div className="section-container">
        <div className="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
          {/* Text */}
          <motion.div
            ref={ref}
            initial="hidden"
            animate={inView ? 'visible' : 'hidden'}
            variants={fadeSlideLeft}
          >
            <p className="section-label">About Me</p>
            <h2 className="section-heading mb-6">
              Building at the intersection of{' '}
              <span className="gradient-text italic">intelligence</span> and craft.
            </h2>
            <div className="space-y-4 text-[var(--fg-muted)] leading-relaxed text-lg">
              <p>
                I'm a Computer Engineering student at FCRIT Navi Mumbai passionate about building high-performance backend systems and elegant, interactive frontend interfaces. My development workflow centers around building with Core Java, C++, Python, and React.
              </p>
              <p>
                With a deep focus on Data Structures, Algorithms, and Object-Oriented Design, I have secured pre-placement offers and built multiple real-world full-stack projects. I also enjoy mentoring juniors and helping peers prepare for tech placements.
              </p>
              <p>
                I'm looking for full-time opportunities where I can solve complex engineering challenges, write clean and efficient code, and ship high-impact software systems.
              </p>
            </div>
          </motion.div>

          {/* Cards */}
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
                <div className="shrink-0 w-10 h-10 rounded-lg bg-[var(--node)]/10 flex items-center 
                                justify-center text-[var(--node)]">
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
