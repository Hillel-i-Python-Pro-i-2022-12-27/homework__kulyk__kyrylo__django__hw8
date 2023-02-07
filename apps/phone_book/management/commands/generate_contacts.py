import logging

from django.core.management import BaseCommand

from apps.phone_book.models import Contact
from apps.phone_book.services.generate_contacts import generate_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            help="How many contacts do you want to generate?",
            type=int,
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        logger = logging.getLogger("django")
        queryset = Contact.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        for contact in generate_contacts(amount=amount, is_mark_as_autogenerated=True):
            contact.save()

        logger.info(f"Current amount of contacts after: {queryset.count()}")