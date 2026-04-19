from admin import Admin
from user import User
from db import USERS, EVENTS, CUPONS

# criação de user
user1 = Admin.create_user('Mateus Rafael', 'mateus777', 'mateusrafael@gmail.com')

# criação de admin
admin1 = Admin.create_admin('Victor Santos', 'vetim123', 'vitor@gmail.com')

# evento criado por user
event1 = user1.create_events(
    "FestTrap",
    "Apenas os goats da cena em ação",
    "2026-12-10",
    "Toledo",
    20
)

# criação de cupom
cupon1 = user1.create_cupon("PROMO10", "2026-12-30", 10, event1.id)
print('cupon criado:', cupon1)


# Listagem


print("\n--- LISTAS ---")
print("USERS:")
for u in USERS:
    print(u)

print("\nEVENTS:")
for e in EVENTS:
    print(e)

print("\nCUPONS:")
for c in CUPONS:
    print(c)


# BUSCAS


print("\n--- BUSCAS ---")
print("Buscar usuário por ID:", User.get_user_by_id(1))
print("Buscar evento por ID:", user1.get_event_by_id(1))
print("Buscar cupom por ID:", user1.get_cupon_by_id(1))


# FILTROS


print("\n--- FILTROS ---")
print("Eventos do usuário:", user1.get_events_by_user())
print("Cupons do evento:", user1.get_cupon_by_event(event1.id))


# UPDATES


print("\n--- UPDATES ---")

# usuário
user1.update_username("Mateus Atualizado")
user1.update_password("nova_senha")
user1.update_email("novo@email.com")

# evento
user1.update_event_title(event1.id, "FestTrap Atualizado")
user1.update_event_description(event1.id, "Nova descrição")
user1.update_event_local(event1.id, "Cascavel")
user1.update_event_base_price(event1.id, 50)

# cupom
user1.update_cupon_title(cupon1.id, "PROMO20")
user1.update_cupon_discount_value(cupon1.id, 20)

print("Usuário atualizado:", user1)
print("Evento atualizado:", user1.get_event_by_id(event1.id))
print("Cupom atualizado:", user1.get_cupon_by_id(cupon1.id))


# descontos


print("\n--- DESCONTO ---")
print("Preço final:", user1.final_price(event1.id))


# DELETE


print("\n--- DELETE ---")

# deletar cupom
print("Removendo cupom:", user1.delete_cupon(cupon1.id))
print("CUPONS após delete:", CUPONS)

# recriar cupom pra testar evento
cupon2 = user1.create_cupon("PROMO5", "2026-12-30", 5, event1.id)

# deletar evento (deve remover cupons também)
print("Removendo evento:", user1.delete_event(event1.id))
print("EVENTS após delete:", EVENTS)
print("CUPONS após delete do evento:", CUPONS)


# ADMIN


print("\n--- ADMIN ---")
print("Todos usuários:", Admin.get_all_users())
print("Buscar admin:", Admin.get_user_by_id(admin1.id))

# deletar usuário
print("Removendo usuário:", Admin.delete_user(user1.id))
print("USERS após delete:", USERS)