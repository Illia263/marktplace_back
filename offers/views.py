from django.shortcuts import render
from rest_framework import generics
from .serializers import OfferSerializer
from .models import Offer
from django_filters.rest_framework import DjangoFilterBackend

#SECURITY FIX
class OfferListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game', 'category', 'is_active']
#SECURITY FIX
class OfferDetailView(generics.RetrieveAPIView):
    permission_classes = []
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = 'uuid'

class GameByNameAndCategoryView(generics.ListAPIView):
   
    serializer_class = OfferSerializer
    permission_classes = []

    def get_queryset(self):
        game_slug = self.kwargs['game_slug']
        category_slug = self.kwargs['category_slug']
        return Offer.objects.filter(
            game__slug=game_slug,
            category__slug=category_slug,
            is_active=True  
        )

class GameByNameView(generics.ListAPIView):
    permission_classes = []
    serializer_class = OfferSerializer
    def get_queryset(self):
        game_slug = self.kwargs['game_slug']
        return Offer.objects.filter(
            game__slug=game_slug,
            is_active=True
        )


# #Супер! Почнемо з найважливішого для будь-якого маркетплейсу — **Безпеки та Авторизації продавця**. Ми не можемо дозволити хакерам створювати товари від твого імені.

# Зараз ми зробимо так, щоб Кайрату (на фронтенд) взагалі не потрібно було передавати поле `seller`. Твій бекенд стане достатньо розумним, щоб сам діставати ідентифікатор користувача з його секретного токена доступу.

# Ось твій план дій із 3 кроків:

# ### Крок 1: Блокуємо поле `seller` для запису

# Відкрий свій `serializers.py` (у папці `offers`). Зараз поле `seller` приймає дані від фронтенду. Нам треба це заборонити, але зробити так, щоб при читанні (GET) покупці все одно бачили, хто продає товар.

# * **Що робити:** У твоєму словнику `extra_kwargs` додай ще одне правило для поля `'seller'`. Тільки цього разу воно має бути **не** `write_only`, а навпаки — **`'read_only': True`**.

# ### Крок 2: Ставимо охоронця на в'юшку

# Переходь у `views.py` (у папці `offers`). Нам треба сказати системі: *"Дивитися на товари можуть абсолютно всі (навіть гості без акаунта), але створювати нові — тільки залогінені юзери"*.

# * **Що робити:** 1. Нагорі файлу зроби імпорт: `from rest_framework import permissions`
# 2. Всередині класу `OfferListCreateView` (там, де в тебе `queryset` та `serializer_class`) додай нову змінну:
# `permission_classes = [permissions.IsAuthenticatedOrReadOnly]`

# ### Крок 3: Магія автоматичного призначення

# Залишаємось у тому ж класі `OfferListCreateView`. Коли користувач відправляє `POST`-запит, DRF бере його дані, проганяє через серіалізатор і викликає вбудовану функцію збереження. Тобі треба "перехопити" цей момент і вставити туди поточного юзера.

# * **Що робити:** Додай всередину класу ось такий метод (зверни увагу на відступи, це функція всередині класу):

# ```python
#     def perform_create(self, serializer):
#         # self.request.user — це і є той юзер, який зараз робить запит
#         serializer.save(seller=self.request.user)

# ```

# Збереш ці три оновлення у своїх файлах? Як тільки зробиш — показуй код, і ми одразу навчимо цю ж саму в'юшку геніально фільтрувати товари за іграми!