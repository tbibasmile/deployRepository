from django.contrib.auth import get_user_model
from django.contrib.auth.management.commands import createsuperuser
from django.db.utils import IntegrityError

class Command(createsuperuser.Command):
    def handle(self, *args, **options):
        options.setdefault('interactive', True)
        email = options.get('email')
        username = options.get('username') or email  # ユーザー名が提供されていない場合は email を使用します
        password = options.get('password')

        if not email:
            self.stderr.write(self.style.ERROR('Email address is required.'))
            return

        if not password:
            self.stderr.write(self.style.ERROR('Invalid password.'))
            return

        User = get_user_model()

        try:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
        except IntegrityError:
            self.stderr.write(self.style.ERROR('Superuser with email %s already exists.' % email))
            return

        if options['verbosity'] >= 1:
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
