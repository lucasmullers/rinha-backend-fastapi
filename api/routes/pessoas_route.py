from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, func

from core.dependencies import get_session
from models.pessoas_model import PessoasModel


router = APIRouter()


@router.post("/", response_model=PessoasModel, status_code=status.HTTP_201_CREATED)
async def post_pessoa(pessoa: PessoasModel, db: AsyncSession = Depends(get_session)):
    try:
        db.add(pessoa)
        await db.commit()
        await db.refresh(pessoa)
        return pessoa
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Request fora do padrão!")


@router.get("/{id}", response_model=PessoasModel, status_code=status.HTTP_200_OK)
async def get_pessoa(id: str, db: AsyncSession = Depends(get_session)):

    async with db as session:
        result = await session.execute(select(PessoasModel).filter(PessoasModel.id == id))
        pessoa: PessoasModel = result.scalar_one_or_none()

        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada")

        return pessoa


@router.get("/", response_model=List[PessoasModel], status_code=status.HTTP_200_OK)
async def get_by_term(t: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(PessoasModel).filter(
            or_(
                PessoasModel.apelido.ilike(f"%{t}%"),
                PessoasModel.nome.ilike(f"%{t}%"),
                func.array_to_string(PessoasModel.stack, ",").ilike(f"%{t}%"),
            )).limit(50))

        pessoas: List[PessoasModel] = result.scalars().all()

        if not pessoas:
            raise HTTPException(status_code=status.HTTP_200_OK, detail=[])

        return pessoas
