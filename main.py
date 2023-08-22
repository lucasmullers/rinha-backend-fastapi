import uvicorn

from fastapi import FastAPI, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from api.routes import main_router
from core.dependencies import get_session
from models.pessoas_model import PessoasModel


app = FastAPI()
app.include_router(main_router)


@app.get("/contagem-pessoas", status_code=status.HTTP_200_OK)
async def contagem_pessoas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(func.count(PessoasModel.id))
        result = await session.execute(query)
        result = result.scalar_one()

        return result


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
