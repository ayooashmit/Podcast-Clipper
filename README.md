# Podcast-Clipper
(currently in development phase)

This project aims to build a production-ready SaaS application that transforms long podcasts into viral short-form clips optimized for YouTube Shorts and TikTok. It integrates AI-driven transcription, active speaker detection, and LLM-based highlight extraction to automatically detect the most engaging podcast moments and crop them precisely to the speaker’s frame. The backend leverages FastAPI, Modal, and Inngest for serverless GPU-accelerated processing and queue-based scalability, while the frontend is powered by Next.js 15, React, TypeScript, and ShadCN UI. A Stripe-based credit system manages user payments, and AWS S3 handles secure media storage. End-to-end automation—from video upload to rendered clip delivery—minimizes manual editing, easing repetitive content-creation tasks by over 90 %. The result is a seamless, scalable platform combining AI, cloud compute, and web engineering to make professional-grade video editing accessible to everyone.

Implementation Steps (Work in Progress):

1.Project Setup: Initialize monorepo with Next.js 15 frontend and FastAPI backend; configure environment variables.

2.Modal + GPU Integration: Enable serverless GPU processing for heavy video workloads (FFMPEGCV, WhisperX).

3.Transcription Module: Implement m-bain/WhisperX for speech-to-text conversion and timestamp alignment.

4.Viral Moment Detection: Use Gemini API LLM to identify compelling story or question segments.

5.Speaker Cropping: Integrate Junhua-Liao/LR-ASD for active-speaker detection and frame cropping.

6.Queue System: Set up Inngest for background jobs and long-running pipeline execution.

7.Storage & Delivery: Upload processed clips to AWS S3, generate presigned URLs for secure access.

8.Payment & Credits: Add Stripe integration with credit-based limits for clip generation.

9.Frontend UI: Build dashboard using Tailwind CSS + ShadCN with upload, queue-status, and billing pages.

10.Deployment: Deploy serverless infrastructure via Modal and Vercel, ensuring monitoring and scalability.
