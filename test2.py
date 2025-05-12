import psycopg2

# Paramètres de connexion
host = "Maguatte-4510.postgres.pythonanywhere-services.com"
port = 14510
database = "postgres"  # Mets ici le nom de ta base si ce n'est pas "postgres"
user = "super"
password = "R#G7qaDfHbwT2gS"  # Remplace par ton vrai mot de passe

try:
    # Connexion
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    print("✅ Connexion réussie !")
    conn.close()

except Exception as e:
    print("❌ Erreur de connexion :", e)
