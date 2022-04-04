from typing import List, Dict
from fastapi import UploadFile
from starlette.responses import StreamingResponse
from fastapi import APIRouter, status, HTTPException

from utils.s3 import S3Loader
from endpoints.base import prefix

router = APIRouter(prefix=prefix)


@router.get("/s3_api/file/{file_path:path}", status_code=status.HTTP_200_OK)
async def get_file(file_path: str):
    s3 = S3Loader(file_path=file_path)
    if s3.object is not None:
        return StreamingResponse(s3.streamer(), media_type=s3.object['ContentType'], headers={
            "Content-Disposition": f"attachment;filename={s3.file_name}"
        })
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")


@router.get("/s3_api/directory/{dir_path:path}", status_code=status.HTTP_200_OK)
async def get_list_files_in_directory(dir_path: str):
    s3 = S3Loader(dir_path=dir_path)
    if 'Contents' in s3.objects:
        return s3.get_file_names()
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Folder isn't exist")


@router.post("/s3_api/{dir_path:path}", response_model=Dict, status_code=status.HTTP_201_CREATED)
async def upload_file(files: List[UploadFile],
                      dir_path: str):
    s3 = S3Loader(files=files, file_path=dir_path)
    if s3.upload_files():
        return {"Files uploaded ": [dir_path + '/' + file.filename for file in files]}
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Couldn't uploaded files")


@router.put("/s3_api/{file_path:path}", status_code=status.HTTP_200_OK)
async def update_file(files: UploadFile,
                      file_path: str):
    s3 = S3Loader(files=[files], file_path=file_path)
    s3.update_file()
    return {"Updated File": file_path}


@router.delete("/s3_api/{file_path:path}", status_code=status.HTTP_200_OK)
async def delete_file(file_path: str):
    s3 = S3Loader(file_path=file_path)
    s3.delete_file()
    return {"Deleted File": file_path}
