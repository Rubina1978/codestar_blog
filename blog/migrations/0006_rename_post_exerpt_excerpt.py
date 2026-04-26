from django.db import migrations


def rename_exerpt_column(apps, schema_editor):
    table_name = "blog_post"
    with schema_editor.connection.cursor() as cursor:
        columns = {
            c.name for c in schema_editor.connection.introspection.get_table_description(cursor, table_name)
        }
        if "exerpt" in columns and "excerpt" not in columns:
            schema_editor.execute(
                'ALTER TABLE "blog_post" RENAME COLUMN "exerpt" TO "excerpt";'
            )


def rename_excerpt_column_back(apps, schema_editor):
    table_name = "blog_post"
    with schema_editor.connection.cursor() as cursor:
        columns = {
            c.name for c in schema_editor.connection.introspection.get_table_description(cursor, table_name)
        }
        if "excerpt" in columns and "exerpt" not in columns:
            schema_editor.execute(
                'ALTER TABLE "blog_post" RENAME COLUMN "excerpt" TO "exerpt";'
            )


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_comment_options_alter_post_options"),
    ]

    operations = [
        migrations.RunPython(rename_exerpt_column, rename_excerpt_column_back),
    ]
