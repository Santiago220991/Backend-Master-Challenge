from typing import Optional
from app.src.exceptions import ProductNotFoundException, ProductRepositoryException
from app.src.core.models import Product 
from app.src.repositories import ProductRepository

from .request import DeleteProductByIdRequest 
from .response import DeleteProductByIdResponse 


class DeleteProductById:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __call__(
            self, request: DeleteProductByIdRequest
    ) -> Optional[DeleteProductByIdResponse]:
        try:
            product_existing = self.product_repository.get_by_id(request.product_id)
            if not product_existing:
                raise ProductNotFoundException(product_id=request.product_id)
            
            response = self.product_repository.delete(request.product_id)
            if not response:
                raise ProductNotFoundException()
            
            return DeleteProductByIdResponse(sucess=True)
        except ProductRepositoryException as e:
            raise e
        
        