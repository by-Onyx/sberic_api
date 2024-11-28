from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.services.file_service import FileService

router = APIRouter(prefix='/file', tags=['file'])

__file_service = FileService()


@router.get('/')
async def get_file(file_name: str):
    try:
        response = __file_service.get_file(file_name)
        return StreamingResponse(
            response,
            media_type="image/png",
            headers={"Content-Disposition": f"attachment; filename={file_name}"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error get file: {str(e)}")
