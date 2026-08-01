from app.database.connection import supabase
import uuid


def upload_complaint_image(file):
    file_extension = file.filename.split(".")[-1]

    file_name = f"{uuid.uuid4()}.{file_extension}"

    file_content = file.file.read()

    response = supabase.storage \
        .from_("complaint-images") \
        .upload(
            file_name,
            file_content,
            {
                "content-type": file.content_type
            }
        )

    image_url = (
        supabase.storage
        .from_("complaint-images")
        .get_public_url(file_name)
    )

    return image_url