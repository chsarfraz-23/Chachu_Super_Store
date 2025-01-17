from django.urls import path
from myapp.views import (
    home_page,
    upload_products,
    paid_services,
    cart,
    check_cart,
    check_plan,
    remove_from_cart,
    choose_plan,
    upload_challan,
    admin_plans,
    front_page,
    view_challan,
    reject_challan,
    login_view,
    logout_main,
    main_products_detail,
    upload_product_on_shop,
    shops_data_home,
    cart_main,
    shop_cart,
    allow_main,
    reject_shop_request,
    verify_shop_f,
    my_shop,
    forget_id,
    admin_verification,
    order_now,
    open_your_shop,
    show_shop_data,
    shopping_stores,
    approve_shop,
    UserSignUp,
)

urlpatterns = [
    path("signup/", UserSignUp.as_view()),
    path("login/main/logout/", logout_main),
    path("main/home/login/main/logout/", logout_main),
    path("main/home/login/main/logout/login/", login_view),
    path("main/home/login/main/logout/login/main/", home_page),
    path("login/main/logout/login/", login_view),
    path("", home_page, name="main"),
    path("logout/", logout_main),
    path("order_now/", order_now),
    path("order_now/check_cart/", check_cart),
    path("order_now/check_cart/remove_from_cart/<int:id>/", remove_from_cart),
    path("check_cart/", check_cart),
    path("check_cart/remove_from_cart/<int:id>/", remove_from_cart),
    path("upload_products/", upload_products),
    path("upload_products/select_plan/", choose_plan),
    path("upload_products/select_plan/upload_challan/", upload_challan),
    path("upload_products/paid_plan/", paid_services),
    path("upload_products/paid_plan/select_plan/", choose_plan),
    path("upload_products/paid_plan/select_plan/upload_challan/", upload_challan),
    path("check_plan/", check_plan),
    path("open_your_shop/", open_your_shop),
    path("open_your_shop/verify_shop/", verify_shop_f),
    path("open_your_shop/verify_shop/shop/<int:id>/", my_shop),
    path("open_your_shop/verify_shop/shop/<int:id>/upload/", upload_product_on_shop),
    path("open_your_shop/verify_shop/forget_data/", forget_id),
    path("shopping_store/", shopping_stores),
    path("shopping_store/shops_data_home/<int:id>/", shops_data_home),
    path("shopping_store/shops_data_home/<int:id>/shops_cart/<int:id2>/", shop_cart),
    path("main_detail/<int:id>/", main_products_detail, name="main-detail"),
    path("main_detail/<int:id>/cart/<int:id2>/", cart_main),
    path("cart/<int:id>/", cart),
    path("main/home/", front_page, name="home"),
    path("main/home/login/", login_view),
    path("main/home/login/main/", home_page, name="main_page"),
    path("main/home/login/main/order_now/", order_now),
    path("main/home/login/main/order_now/check_cart/", check_cart, name="check-cart"),
    path(
        "main/home/login/main/order_now/check_cart/remove_from_cart/<int:id>/",
        remove_from_cart,
    ),
    path("main/home/login/main/check_cart/", check_cart),
    path(
        "main/home/login/main/check_cart/remove_from_cart/<str:id>/", remove_from_cart
    ),
    path("main/home/login/main/upload_products/", upload_products),
    path("main/home/login/main/upload_products/select_plan/", choose_plan),
    path(
        "main/home/login/main/upload_products/select_plan/upload_challan/",
        upload_challan,
    ),
    path("main/home/login/main/upload_products/paid_plan/", paid_services),
    path("main/home/login/main/upload_products/paid_plan/select_plan/", choose_plan),
    path(
        "main/home/login/main/upload_products/paid_plan/select_plan/upload_challan/",
        upload_challan,
    ),
    path("main/home/login/main/check_plan/", check_plan),
    path("main/home/login/main/open_your_shop/", open_your_shop),
    path("main/home/login/main/open_your_shop/verify_shop/", verify_shop_f),
    path("main/home/login/main/open_your_shop/verify_shop/forget_data/", forget_id),
    path("main/home/login/main/open_your_shop/verify_shop/shop/<int:id>/", my_shop),
    path("main/home/login/main/shopping_store/", shopping_stores),
    path(
        "main/home/login/main/shopping_store/shops_data_home/<int:id>/", shops_data_home
    ),
    path(
        "main/home/login/main/shopping_store/shops_data_home/<int:id>/shops_cart/<int:id2>/",
        shop_cart,
    ),
    path("main/home/login/main/cart/<str:id>", cart),
    path("main/home/login/main/main_detail/<int:id>/", main_products_detail),
    path("main/home/login/main/main_detail/<int:id>/cart/<int:id2>/", cart_main),
    path("home/", front_page),
    path("login/", login_view),
    path("login/main/", home_page),
    path("login/main/main_detail/<int:id>/", main_products_detail),
    path("login/main/main_detail/<int:id>/cart/<int:id2>/", cart_main),
    path("login/main/shopping_store/", shopping_stores),
    path("login/main/shopping_store/shops_data_home/<int:id>/", shops_data_home),
    path(
        "login/main/shopping_store/shops_data_home/<int:id>/shops_cart/<int:id2>/",
        shop_cart,
    ),
    path("login/main/open_your_shop/", open_your_shop),
    path("login/main/open_your_shop/verify_shop/", verify_shop_f),
    path("login/main/open_your_shop/verify_shop/forget_data/", forget_id),
    path("login/main/open_your_shop/verify_shop/shop/<int:id>/", my_shop),
    path(
        "login/main/open_your_shop/verify_shop/shop/<int:id>/upload/",
        upload_product_on_shop,
    ),
    path("upload/verify_shop/", verify_shop_f),
    path("upload/verify_shop/shop/<int:id>/", my_shop),
    path("upload/verify_shop/shop/<int:id>/upload/", upload_product_on_shop),
    path("login/main/order_now/", order_now),
    path("login/main/order_now/check_cart/", check_cart),
    path(
        "login/main/order_now/check_cart/remove_from_cart/<int:id>/", remove_from_cart
    ),
    path("main/order_now/", order_now),
    path("main/order_now/check_cart/", check_cart),
    path("main/order_now/check_cart/remove_from_cart/<int:id>/", remove_from_cart),
    path("main/", home_page),
    path("main/open_your_shop/", open_your_shop),
    path("main/open_your_shop/verify_shop/", verify_shop_f),
    path("main/open_your_shop/verify_shop/forget_data/", forget_id),
    path("main/open_your_shop/verify_shop/shop/<int:id>/", my_shop),
    path("sarfraz/", admin_plans),
    path("sarfraz/show_shop_data/", show_shop_data),
    path("sarfraz/show_shop_data/reject_shop_request/<int:id>/", reject_shop_request),
    path("sarfraz/show_shop_data/approve_shop/<int:id>/", approve_shop),
    path("main/sarfraz/", admin_plans),
    path("sarfraz/view_challans/", view_challan),
    path("sarfraz/view_challans/allowed/", allow_main),
    path("sarfraz/view_challans/reject/<int:id>/", reject_challan),
    path("login/main/check_plan/", check_plan),
    path("main/check_plan/", check_plan),
    path("main/upload_products/", upload_products),
    path("login/main/upload_products/", upload_products),
    path("main/upload_products/paid_plan/", paid_services),
    path("login/main/upload_products/paid_plan/", paid_services),
    path("main/upload_products/paid_plan/select_plan/", choose_plan),
    path("main/upload_products/select_plan/", choose_plan),
    path("main/upload_products/select_plan/upload_challan/", upload_challan),
    path("login/main/upload_products/paid_plan/", paid_services),
    path("login/main/upload_products/select_plan/", choose_plan),
    path("login/main/upload_products/select_plan/upload_challan/", upload_challan),
    path("main/upload_products/paid_plan/select_plan/upload_challan/", upload_challan),
    path(
        "login/main/upload_products/paid_plan/select_plan/upload_challan/",
        upload_challan,
    ),
    path("main/cart/<int:id>/", cart),
    path("main/cart/<int:id>/", cart),
    path("login/main/cart/<int:id>/", cart),
    path("main/check_cart/", check_cart),
    path("login/main/check_cart/", check_cart),
    path("main/check_cart/remove_from_cart/<int:id>/", remove_from_cart),
    path("login/main/check_cart/remove_from_cart/<int:id>/", remove_from_cart),
    path("sarfraz/admin_verification/", admin_verification),
    # Api section
    path("shop_approved_api/", approve_shop),
]
