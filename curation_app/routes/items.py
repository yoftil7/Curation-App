from flask_restx import Namespace, Resource, fields
from models.item import Item


api = Namespace('items', description='Item APIs')

item_model = api.model('Item', {
    'content': fields.String(required=True, description='The content of the item')
})

@api.route('/')
class ItemList(Resource):
    @api.doc('list_items')
    def get(self):
        items = Item.get_all()
        return [{'id': str(item['_id']), 'content': item['content'], 'status': item['status']} for item in items]


    @api.expect(item_model)
    @api.doc('create_item')
    def post(self):
        data = api.payload
        new_item = Item(content=data['content'])
        new_item.save()
        return {'message': 'Item created'}, 201


@api.route('/<id>')
@api.param('id', 'The item identifier')
class ItemResource(Resource):
    @api.doc('get_item')
    def get(self, id):
        item = Item.get_by_id(id)
        if item:
            return {'id': str(item['_id']), 'content': item['content'], 'status': item['status']}
        api.abort(404, f"Item {id} does not exist")


@api.route('/<id>/correct')
@api.param('id', 'The item identifier')
class MarkCorrect(Resource):
    @api.doc('mark_correct')
    def post(self, id):
        Item.update_status(id, 'correct')
        return {'message': 'Item marked as correct'}


@api.route('/<id>/not_correct')
@api.param('id', 'The item identifier')
class MarkNotCorrect(Resource):
    @api.doc('mark_not_correct')
    def post(self, id):
        Item.update_status(id, 'not_correct')
        return {'message': 'Item marked as not correct'}


@api.route('/<id>/not_sure')
@api.param('id', 'The item identifier')
class MarkNotSure(Resource):
    @api.doc('mark_not_sure')
    def post(self, id):
        Item.update_status(id, 'not_sure')
        return {'message': 'Item marked as not sure'}
















