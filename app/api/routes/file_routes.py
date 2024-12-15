from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.services.help_services.file_service import get_file

router = APIRouter(prefix='/file', tags=['file'])


@router.get('/')
async def get_minio_file(file_name: str):
    try:
        response = get_file(file_name)
        return StreamingResponse(
            response,
            media_type="image/png",
            headers={"Content-Disposition": f"attachment; filename={file_name}"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error get file: {str(e)}")
