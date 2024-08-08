import pytest

from app.src.use_cases.product.delete.request import DeleteProductByIdRequest
from app.src.use_cases.product.delete.use_case import DeleteProductById
from app.src.use_cases.product.delete.response import DeleteProductByIdResponse
from app.src.repositories.product_repository import ProductRepository
from app.src.exceptions import ProductNotFoundException


def test_delete_product_sucess(mocker):
    mock_product_repository = mocker.Mock(spec=ProductRepository)
    mock_product_repository.get_byid.return_value = {"product_id": "123"}
    mock_product_repository.delete.return_value = True

    delete_product_use_case = DeleteProductById(mock_product_repository)
    request = DeleteProductByIdRequest(product_id="123")
    response = delete_product_use_case(request)

    assert response.sucess is True

    def test_delete_product_not_found(mocker):
        mock_product_repository = mocker.Mock(spec=ProductRepository)
        mock_product_repository.get_byid.return_value = None
        mock_product_repository.delete.return_value = False

        delete_product_use_case = DeleteProductById(mock_product_repository)
        request = DeleteProductByIdRequest(product_id="123")
        with pytest.raises(ProductNotFoundException):
            delete_product_use_case(request)

