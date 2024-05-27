import json
from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # Проверяем, что data является словарем
        if isinstance(data, dict):
            token = data.get('token', None)
            if token is not None and isinstance(token, bytes):
                data['token'] = token.decode('utf-8')
            # Наконец, мы можем отобразить наши данные в простанстве имен 'user'.
            return json.dumps({
                'user': data
            })
        # Если data не является словарем, просто возвращаем его
        else:
            return super().render(data, media_type, renderer_context)