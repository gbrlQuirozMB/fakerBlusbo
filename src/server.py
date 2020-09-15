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
    # r = Response(json.dumps(menu), status=200)
    with open('menu.json', 'r') as j:
        jsonData = json.load(j)
    r = Response(json.dumps(jsonData), status=200)
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/detalle-producto/<id>', methods=['GET'])
def getDetalleProducto(id):
    if id != '1':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('detalle-producto.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/detalle-producto/recomendados/<sku>', methods=['GET'])
def getDetalleProductoRecomendados(sku):
    if sku != 'B68496':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('detalle-producto-recomendados.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r

# ---------


@api.route('/hombre/temporada/<id>', methods=['GET'])
def getHombre(id):
    if id != '1':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('hombre-temporada.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/hombre/temporada/<idTemporada>/categoria/<idCategoria>', methods=['GET'])
def getHombreCategoria(idTemporada, idCategoria):
    if idTemporada != '1' or idCategoria != '1':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('hombre-temporada-categoria.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/mujer/temporada/<id>', methods=['GET'])
def getMujer(id):
    if id != '1':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('mujer-temporada.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/mujer/temporada/<idTemporada>/categoria/<idCategoria>', methods=['GET'])
def getMujerCategoria(idTemporada, idCategoria):
    if idTemporada != '1' or idCategoria != '1':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('mujer-temporada-categoria.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/mujer/temporada/<id>/categorias', methods=['GET'])
def getMujerCategorias(id):
    if id != '1':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('mujer-temporada-categorias.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r

@api.route('/rebajas/<id>', methods=['GET'])
def getRebajas(id):
    if id != '1':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('rebajas.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@api.route('/rebajas/temporada/<idTemporada>/categoria/<idCategoria>', methods=['GET'])
def getRebajasTemporada(idTemporada, idCategoria):
    if idTemporada != '1' or idCategoria != '1':
        r = Response(json.dumps(notFound), status=404)
    else:
        with open('rebajas-categoria.json', 'r') as j:
            jsonData = json.load(j)
        r = Response(json.dumps(jsonData), status=200)

    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


# ---------FALTAN POR DEFINIR

# @api.route('/completa-compra', methods=['GET'])
# def getCompletaCompra():
#     with open('completa-compra.json', 'r') as j:
#         jsonData = json.load(j)
#     r = Response(json.dumps(jsonData), status=200)
#     r.headers["Content-Type"] = "application/json; charset=utf-8"
#     return r


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
