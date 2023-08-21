from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.dependencies import get_session
from models.pessoas_model import PessoasModel


router = APIRouter()


@router.post("/", response_model=PessoasModel, status_code=status.HTTP_201_CREATED)
async def post_pessoa(pessoa: PessoasModel, db: AsyncSession = Depends(get_session)):

    db.add(pessoa)
    await db.commit()
    await db.refresh(pessoa)
    return pessoa


@router.get("/{id}", response_model=PessoasModel, status_code=status.HTTP_200_OK)
async def get_pessoa(id: str, db: AsyncSession = Depends(get_session)):

    async with db as session:
        query = select(PessoasModel).filter(PessoasModel.id == id)
        result = await session.execute(query)
        result = result.scalars().one_or_none()

        if not result:
            HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada")

        return result
