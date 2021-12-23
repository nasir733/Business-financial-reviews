import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from reviews.models import Review, ReviewComment


class Command(BaseCommand):

    help = "It seeds the DB with tons of stuff"

    def handle(self, *args, **options):
        reviews_seeder = Seed.seeder()
        user_seeder = Seed.seeder()
        user_seeder.add_entity(
            User, 20, {"is_staff": False, "is_superuser": False})
        user_seeder.execute()

        users = User.objects.all()
        reviews_seeder.add_entity(Review, 100, {
            'business': lambda x: random.randint(0, 1000),
            'user': lambda x: random.randint(0, 2),
            'review': lambda x: random.randint(0, 1000),
            'content': lambda x: random.randint(0, 1000),
            'rating': lambda x: reviews_seeder.faker.catch_phrase(),

            # 'nickname': lambda x: reviews_seeder.faker.email(),

        })

        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
