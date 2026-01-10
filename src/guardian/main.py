from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app with metadata for Swagger/OpenAPI
app = FastAPI(
    title="GuardianAuth API",
    description="Enterprise Identity & Access Manager with JWT Rotation and RBAC.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS for US-based Enterprise security standards
# In production, 'allow_origins' should be restricted to specific domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["System"])
async def health_check():
    """
    Standard health check endpoint for container orchestration (Kubernetes/Docker).
    Returns 'ok' to signal the service is ready to accept traffic.
    """
    return {
        "status": "ok",
        "service": "guardian-auth",
        "version": "0.1.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.guardian.main:app", host="0.0.0.0", port=8000, reload=True)