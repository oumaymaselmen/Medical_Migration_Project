// On se positionne sur la base de données
use Healthcare

// 1. L'ADMINISTRATEUR (Droits totaux)
db.createUser({
  user: "Admin_Projet",
  pwd: "admin_password_123",
  roles: [{ role: "root", db: "admin" }]
})

// 2. USER_MEDICAL (Lecture et Écriture)
db.createUser({
  user: "User_Medical",
  pwd: "medical_password_123",
  roles: [{ role: "readWrite", db: "Healthcare" }]
})

// 3. ANALYSTE (Lecture seule)
db.createUser({
  user: "Analyste",
  pwd: "analyst_password_456",
  roles: [{ role: "read", db: "Healthcare" }]
})

print("Les 3 utilisateurs (Admin, Médical, Analyste) ont été créés !");
