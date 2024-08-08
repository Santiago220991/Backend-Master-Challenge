from typing import Optional
from app.src.exceptions import ProductNotFoundException, ProductRepositoryException #may add more exceptions. 
from app.src.core.models import Product 
from app.src.repositories import ProductRepository

from .request import DeleteProductByIdRequest 
from .response import DeleteProductByIdResponse 


class DeleteProductById:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __call__(self, request: DeleteProductByIdRequest) -> DeleteProductByIdResponse:
        try:
            existing_product = self.product_repository.get_by_id(request.product_id)
            if existing_product is None:
                raise ProductNotFoundException(product_id=request.product_id)
            response = self.product_repository.delete_by_id(request.product_id)
            return response
        except ProductRepositoryException as e:
            raise e