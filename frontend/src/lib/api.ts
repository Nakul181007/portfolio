import axios from 'axios'
import type { Project, Skill, Experience, ContactRequest, ContactResponse } from '@/types'

const api = axios.create({
  // Set VITE_API_URL to the deployed API origin plus /api in production.
  // Local development continues to use the Vite /api proxy.
  baseURL: import.meta.env.VITE_API_URL || '/api',
  headers: { 'Content-Type': 'application/json' },
})

export const fetchProjects = (): Promise<Project[]> =>
  api.get<Project[]>('/projects/').then((r) => r.data)

export const fetchSkills = (): Promise<Skill[]> =>
  api.get<Skill[]>('/skills/').then((r) => r.data)

export const fetchExperience = (): Promise<Experience[]> =>
  api.get<Experience[]>('/experience/').then((r) => r.data)

export const submitContact = (data: ContactRequest): Promise<ContactResponse> =>
  api.post<ContactResponse>('/contact/', data).then((r) => r.data)

export default api
