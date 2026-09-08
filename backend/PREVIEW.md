# Hosting preview

Vercel uses its FastAPI builder. The source configuration clears the old
long-running Uvicorn build command and manual system-pip installation.

When `VERCEL_ENV=preview`, headset data is synthetic and session files use
temporary storage. Sessions can disappear or differ across function instances.
This preview is for checking deployment compatibility, not durable study records.
Local runs retain their existing device selection and `data/` directory.

Run `python -m unittest test_preview` in the backend virtual environment to check
the preview boundary. Do not send real audio or provider requests during smoke
tests. Audio processing still needs FFmpeg, libmagic, and a configured provider.

A physical headset needs a process beside the device. A hosted production
backend needs an explicit device bridge, durable session storage, authentication,
and an allowed frontend origin before it can replace the local workflow.
