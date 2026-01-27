from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import time

app = FastAPI(title="3D Scanner API Gateway")

# --- In-memory scan storage (simulation) ---
scans = {}


class ScanResponse(BaseModel):
    scan_id: str
    status: str


@app.post("/scan/start", response_model=ScanResponse)
def start_scan():
    scan_id = str(uuid.uuid4())

    scans[scan_id] = {
        "status": "running",
        "started_at": time.time()
    }

    return ScanResponse(scan_id=scan_id, status="running")


@app.get("/scan/{scan_id}/status")
def scan_status(scan_id: str):
    scan = scans.get(scan_id)

    if not scan:
        return {"error": "Scan not found"}

    # simulate completion after 5 seconds
    if time.time() - scan["started_at"] > 5:
        scan["status"] = "completed"

    return {
        "scan_id": scan_id,
        "status": scan["status"]
    }


@app.get("/scan/{scan_id}/result")
def scan_result(scan_id: str):
    scan = scans.get(scan_id)

    if not scan:
        return {"error": "Scan not found"}

    if scan["status"] != "completed":
        return {"error": "Scan not finished yet"}

    return {
        "scan_id": scan_id,
        "point_cloud": "simulated_point_cloud_data.xyz"
    }
