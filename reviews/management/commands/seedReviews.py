import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import CustomUser as User
from reviews.models import Review, ReviewComment
from companydashboard.models import BusinessProfile


class Command(BaseCommand):

    help = "It seeds the DB with tons of stuff"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews do you want to create?"
        )
        parser.add_argument("--company", type=str, default='',
                            help="Which company do you want to seed?")

    def handle(self, *args, **options):
        reviews_seeder = Seed.seeder()
        # user_seeder = Seed.seeder()
        # user_seeder.add_entity(
        #     User, 20, {"is_staff": False, "is_superuser": False})
        # user_seeder.execute()
        businessProfiles = BusinessProfile.objects.filter(
            name=options.get('company')).first()
        users = User.objects.all()
        reviews_seeder.add_entity(Review, options.get("number"), {
            'business': lambda x: random.choice(businessProfiles),
            'user': lambda x: random.choice(users),

            'review': lambda x: " ".join(),
            'content': lambda x: " ".join(),
            'rating': lambda x: random.randint(3, 5),

            # 'nickname': lambda x: reviews_seeder.faker.email(),

        })
        reviews_seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
