#Implementacion con FastAPI para generador de QRs
#Autores: Alfonso Garcia Yague & Emmanuel Acosta

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import qrcode
from io import BytesIO

app = FastAPI()

class QRData(BaseModel):
    data: str

#Ruta Post: Requiere que se mande por body la data
@app.post("/generate-qr/")
async def generate_qr(qr_data: QRData):
    if not qr_data.data:
        raise HTTPException(status_code=400, detail="No data provided for QR code generation.")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data.data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return StreamingResponse(img_byte_arr, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
