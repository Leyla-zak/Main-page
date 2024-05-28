import json

from rest_framework.renderers import JSONRenderer

class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # Проверяем, что data является словарем
        if isinstance(data, dict):
            # Проверяем, есть ли ключ "user" в data
            if 'user' in data:
                user_data = data['user']
                # Если в user_data есть ключ "detail", значит это ошибка
                if 'detail' in user_data:
                    # Позволим стандартному JSONRenderer обрабатывать ошибку.
                    return super(UserJSONRenderer, self).render(data)
                # Если в user_data нет ключа "detail", значит это обычные данные пользователя
                else:
                    # Наконец, мы можем отобразить наши данные в простанстве имен 'user'.
                    return json.dumps({
                        'user': user_data
                    })
            # Если в data нет ключа "user", проверяем, есть ли ключ "detail"
            elif 'detail' in data:
                # Позволим стандартному JSONRenderer обрабатывать ошибку.
                return super(UserJSONRenderer, self).render(data)
            # Если в data нет ключа "user" и "detail", значит это обычные данные (не объект пользователя)
            else:
                return super().render(data, media_type, renderer_context)
        # Если data не является словарем, просто возвращаем его
        else:
            return super().render(data, media_type, renderer_context)