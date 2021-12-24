import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import CustomUser as User
from reviews.models import Review, ReviewComment
from companydashboard.models import BusinessProfile


class Command(BaseCommand):

    help = "It seeds the DB with tons of stuff"

    def handle(self, *args, **options):
        reviews_seeder = Seed.seeder()
        user_seeder = Seed.seeder()
        user_seeder.add_entity(
            User, 20, {"is_staff": False, "is_superuser": False})
        user_seeder.execute()
        businessProfiles = BusinessProfile.objects.all()
        users = User.objects.all()
        reviews_seeder.add_entity(Review, 100, {
            'business': lambda x: random.choice(businessProfiles),
            'user': lambda x: random.choice(users),
            'review': lambda x: reviews_seeder.faker.catch_phrase(),
            'content': lambda x: reviews_seeder.faker.catch_phrase(),
            'rating': lambda x: random.randint(3, 5),

            # 'nickname': lambda x: reviews_seeder.faker.email(),

        })
        reviews_seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
