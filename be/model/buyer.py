from flask import Blueprint
from flask import request
from flask import jsonify
from be.model.buyer import Buyer

# 创建蓝图，定义 URL 前缀为 "/buyer"
bp_buyer = Blueprint("buyer", __name__, url_prefix="/buyer")


# 创建新订单
@bp_buyer.route("/new_order", methods=["POST"])
def new_order():
    # 获取请求中的 JSON 数据
    user_id: str = request.json.get("user_id")
    store_id: str = request.json.get("store_id")
    books: [] = request.json.get("books")
    id_and_count = []  # 用于存储书籍ID和数量
    for book in books:
        book_id = book.get("id")
        count = book.get("count")
        id_and_count.append((book_id, count))  # 将书籍ID和数量加入列表

    # 调用 Buyer 类的 new_order 方法创建新订单
    b = Buyer()
    code, message, order_id = b.new_order(user_id, store_id, id_and_count)
    return jsonify({"message": message, "order_id": order_id}), code  # 返回订单创建的结果


# 支付订单
@bp_buyer.route("/payment", methods=["POST"])
def payment():
    # 获取请求中的 JSON 数据
    user_id: str = request.json.get("user_id")
    order_id: str = request.json.get("order_id")
    password: str = request.json.get("password")
    
    # 调用 Buyer 类的 payment 方法进行支付
    b = Buyer()
    code, message = b.payment(user_id, password, order_id)
    return jsonify({"message": message}), code  # 返回支付结果


# 充值账户余额
@bp_buyer.route("/add_funds", methods=["POST"])
def add_funds():
    # 获取请求中的 JSON 数据
    user_id = request.json.get("user_id")
    password = request.json.get("password")
    add_value = request.json.get("add_value")
    
    # 调用 Buyer 类的 add_funds 方法进行账户充值
    b = Buyer()
    code, message = b.add_funds(user_id, password, add_value)
    return jsonify({"message": message}), code  # 返回充值结果


# 获取订单历史
@bp_buyer.route("/get_order_history", methods=["POST"])
def get_order_history():
    user_id = request.json.get("user_id")
    
    # 调用 Buyer 类的 get_order_history 方法获取订单历史
    b = Buyer()
    code, message, _ = b.get_order_history(user_id)
    return jsonify({"message": message}), code  # 返回订单历史


# 取消订单
@bp_buyer.route("/cancel_order", methods=["POST"])
def cancel_order():
    user_id = request.json.get("user_id")
    order_id = request.json.get("order_id")
    
    # 调用 Buyer 类的 cancel_order 方法取消订单
    b = Buyer()
    code, message = b.cancel_order(user_id, order_id)
    return jsonify({"message": message}), code  # 返回取消订单结果


# 确认收货
@bp_buyer.route("/receive_order", methods=["POST"])
def receive_order():
    user_id = request.json.get("user_id")
    order_id = request.json.get("order_id")
    
    # 调用 Buyer 类的 receive_order 方法确认收货
    b = Buyer()
    code, message = b.receive_order(user_id, order_id)
    return jsonify({"message": message}), code  # 返回收货确认结果


# 获取收藏夹中的图书
@bp_buyer.route("/get_collection", methods=["POST"])
def get_collection():
    user_id = request.json.get("user_id")
    
    # 调用 Buyer 类的 get_collection 方法获取用户收藏的图书
    b = Buyer()
    code, message = b.get_collection(user_id=user_id)
    return jsonify({"message": message}), code  # 返回收藏夹中的图书


# 收藏图书
@bp_buyer.route("/collect_book", methods=["POST"])
def collect_book():
    user_id = request.json.get("user_id")
    book_id = request.json.get("book_id")
    
    # 调用 Buyer 类的 collect_book 方法将图书加入收藏
    b = Buyer()
    code, message = b.collect_book(user_id=user_id, book_id=book_id)
    return jsonify({"message": message}), code  # 返回收藏图书的结果


# 取消收藏图书
@bp_buyer.route("/uncollect_book", methods=["POST"])
def uncollect_book():
    user_id = request.json.get("user_id")
    book_id = request.json.get("book_id")
    
    # 调用 Buyer 类的 uncollect_book 方法取消收藏图书
    b = Buyer()
    code, message = b.uncollect_book(user_id=user_id, book_id=book_id)
    return jsonify({"message": message}), code  # 返回取消收藏的结果


# 获取商店收藏
@bp_buyer.route("/get_store_collection", methods=["POST"])
def get_store_collection():
    user_id = request.json.get("user_id")
    
    # 调用 Buyer 类的 get_store_collection 方法获取商店收藏
    b = Buyer()
    code, message = b.get_store_collection(user_id=user_id)
    return jsonify({"message": message}), code  # 返回商店收藏的结果


# 收藏商店
@bp_buyer.route("/collect_store", methods=["POST"])
def collect_store():
    user_id = request.json.get("user_id")
    store_id = request.json.get("store_id")
    
    # 调用 Buyer 类的 collect_store 方法将商店加入收藏
    b = Buyer()
    code, message = b.collect_store(user_id=user_id, store_id=store_id)
    return jsonify({"message": message}), code  # 返回收藏商店的结果


# 取消收藏商店
@bp_buyer.route("/uncollect_store", methods=["POST"])
def uncollect_store():
    user_id = request.json.get("user_id")
    store_id = request.json.get("store_id")
    
    # 调用 Buyer 类的 uncollect_store 方法取消收藏商店
    b = Buyer()
    code, message = b.uncollect_store(user_id=user_id, store_id=store_id)
    return jsonify({"message": message}), code  # 返回取消收藏商店的结果
