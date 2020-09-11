from flask import Flask, json, Response, request


created = {
    "status": {"code": 201, "message": "creado correctamente"}
}

updated = {
    "status": {"code": 201, "message": "modificado correctamente"}
}

deleted = {
    "status": {"code": 200, "message": "borrado correctamente"}
}

notFound = {
    "status": {"code": 404, "message": "datos no encontrados"}
}

badRequest = {
    "status": {"code": 400, "message": "datos introducidos incorrectos"}
}

conflict = {
    "status": {"code": 409, "message": "descripcion del error"}
}

internal = {
    "status": {"code": 400, "message": "error interno del servidor"}
}

api = Flask(__name__)


@api.route('/menu', methods=['GET'])
def getMenu():
    with open('menu.json', 'r') as j:
        jsonData = json.load(j)
    # r = Response(json.dumps(menu), status=200)
    r = Response(json.dumps(jsonData), status=200)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/detalle-producto/1', methods=['GET'])
def getDetalleProducto():
    # r = Response(json.dumps(detalleProducto), status=200)
    with open('detalle-producto.json', 'r') as j:
        jsonData = json.load(j)
    r = Response(json.dumps(jsonData), status=200)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/detalle-producto/recomendados/B68496', methods=['GET'])
def getDetalleProductoRecomendados():
    # r = Response(json.dumps(detalleProductoRecomendados), status=200)
    with open('detalle-producto-recomendados.json', 'r') as j:
        jsonData = json.load(j)
    r = Response(json.dumps(jsonData), status=200)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/prueba', methods=['POST'])
def postPrueba():
    content = request.get_json()
    # print(content)
    # print(content['saludo'])
    # print(content['numero'])
    if content['numero'] != 1:
        r = Response(json.dumps(badRequest), status=400)
    else:
        r = Response(json.dumps(created), status=201)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r

# ---------FALTAN POR DEFINIR


@api.route('/detalle-producto', methods=['POST'])
def postDetalleProducto():
    r = Response(json.dumps(created), status=201)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/detalle-producto/1', methods=['PUT'])
def putDetalleProducto():
    r = Response(json.dumps(updated), status=200)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/detalle-producto/1', methods=['DELETE'])
def deleteDetalleProducto():
    r = Response(json.dumps(deleted), status=200)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


if __name__ == '__main__':
    api.run()
