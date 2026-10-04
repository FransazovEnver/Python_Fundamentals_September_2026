body_parts = []

for _ in range(3):
    parts = input()
    body_parts.append(parts)

body_parts[0], body_parts[2] = body_parts[2], body_parts[0]

print(body_parts)