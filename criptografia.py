from collections import Counter

MAX_MSG_LEN = 128

COMMON_WEAK_KEYS = {
    "senha", "admin", "password", "qwerty", "abc", "letmein",
    "segredo", "navio", "chave", "teste"
}


def is_ascii_letter(ch: str) -> bool:
    """Retorna True apenas para letras de A a Z, maiúsculas ou minúsculas."""
    return ("A" <= ch <= "Z") or ("a" <= ch <= "z")


def normalize_key(key: str) -> str:
    """Mantém apenas letras do alfabeto usado pela cifra de Vigenère."""
    return "".join(ch for ch in key if is_ascii_letter(ch))


def vigenere_encrypt(message: str, key: str) -> str:
    """Cifra letras com Vigenère e preserva os demais caracteres."""
    k = normalize_key(key)
    if not k:
        raise ValueError("A chave precisa conter pelo menos uma letra de A a Z.")

    out = []
    key_index = 0

    for ch in message:
        if is_ascii_letter(ch):
            base = ord("A") if ch.isupper() else ord("a")
            msg_pos = ord(ch) - base

            key_char = k[key_index % len(k)]
            key_base = ord("A") if key_char.isupper() else ord("a")
            key_pos = ord(key_char) - key_base

            encrypted_pos = (msg_pos + key_pos) % 26
            out.append(chr(base + encrypted_pos))
            key_index += 1
        else:
            out.append(ch)

    return "".join(out)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Decifra letras com Vigenère usando a mesma regra de avanço da chave."""
    k = normalize_key(key)
    if not k:
        raise ValueError("A chave precisa conter pelo menos uma letra de A a Z.")

    out = []
    key_index = 0

    for ch in ciphertext:
        if is_ascii_letter(ch):
            base = ord("A") if ch.isupper() else ord("a")
            cipher_pos = ord(ch) - base

            key_char = k[key_index % len(k)]
            key_base = ord("A") if key_char.isupper() else ord("a")
            key_pos = ord(key_char) - key_base

            decrypted_pos = (cipher_pos - key_pos) % 26
            out.append(chr(base + decrypted_pos))
            key_index += 1
        else:
            out.append(ch)

    return "".join(out)


def key_strength(key: str) -> dict:
    """Avalia a chave por tamanho, variedade, diversidade e previsibilidade."""
    reasons = []
    tips = []
    score = 0

    raw = key.strip()
    k = normalize_key(raw)

    if not raw:
        return {
            "score": 0,
            "label": "Fraca",
            "reasons": ["Chave vazia."],
            "tips": ["Digite uma chave com letras."]
        }

    if not k:
        return {
            "score": 0,
            "label": "Fraca",
            "reasons": ["A chave não contém letras válidas para a cifra."],
            "tips": ["Use letras de A a Z e evite escolhas óbvias."]
        }

    if k != raw:
        reasons.append(
            f"Somente letras de A a Z são consideradas. Chave efetiva: '{k}'"
        )

    length = len(k)
    if length <= 4:
        reasons.append("A chave efetiva é muito curta.")
    elif length <= 7:
        score += 1
        reasons.append("A chave possui tamanho intermediário.")
    elif length <= 11:
        score += 2
        reasons.append("A chave possui bom tamanho.")
    else:
        score += 3
        reasons.append("A chave possui tamanho elevado para esta demonstração.")

    has_lower = any(c.islower() for c in raw)
    has_upper = any(c.isupper() for c in raw)
    if has_lower and has_upper:
        score += 1
        reasons.append("A chave mistura letras maiúsculas e minúsculas.")
    else:
        reasons.append("A chave utiliza apenas um padrão de capitalização.")

    unique_ratio = len(set(k.lower())) / length
    if unique_ratio >= 0.70 and length >= 8:
        score += 2
        reasons.append("A chave apresenta boa diversidade de letras.")
    elif unique_ratio >= 0.45:
        score += 1
        reasons.append("A chave apresenta diversidade moderada de letras.")
    else:
        reasons.append("A chave apresenta pouca diversidade de letras.")

    counts = Counter(k.lower())
    _, most_common_count = counts.most_common(1)[0]
    if length >= 5 and most_common_count / length >= 0.60:
        score -= 2
        reasons.append("A mesma letra aparece em excesso, formando um padrão previsível.")

    if k.lower() in COMMON_WEAK_KEYS:
        score -= 2
        reasons.append("A chave corresponde a uma palavra muito previsível.")

    score = max(0, score)

    if score <= 2:
        label = "Fraca"
    elif score <= 4:
        label = "Média"
    else:
        label = "Forte"

    if label != "Forte":
        tips = [
            "Use uma chave mais longa.",
            "Evite palavras previsíveis e repetições.",
            "Prefira maior diversidade de letras."
        ]

    return {
        "score": score,
        "label": label,
        "reasons": reasons,
        "tips": tips
    }


def read_limited_message(prompt: str) -> str:
    msg = input(prompt)
    if len(msg) > MAX_MSG_LEN:
        raise ValueError(f"A mensagem excede {MAX_MSG_LEN} caracteres.")
    return msg


def main():
    print("=== Ferramenta de Criptografia com Vigenère ===")

    while True:
        print("\nEscolha uma opção:")
        print("1. Cifrar mensagem")
        print("2. Decifrar mensagem")
        print("3. Sair")

        choice = input("Opção: ").strip()

        if choice == "3":
            print("Encerrando.")
            break

        if choice not in {"1", "2"}:
            print("Opção inválida.")
            continue

        try:
            key = input("Digite a chave: ")
            strength = key_strength(key)

            print(f"\nForça da chave: {strength['label']} com pontuação {strength['score']}")
            for reason in strength["reasons"]:
                print(f"• {reason}")

            if strength.get("tips"):
                print("Dicas:")
                for tip in strength["tips"]:
                    print(f"• {tip}")

            if choice == "1":
                message = read_limited_message(
                    "\nDigite a mensagem com até 128 caracteres: "
                )
                cipher = vigenere_encrypt(message, key)
                recovered = vigenere_decrypt(cipher, key)

                print("\nResultado")
                print("Original :", message)
                print("Cifrado  :", cipher)
                print("Decifrado:", recovered)
            else:
                ciphertext = read_limited_message(
                    "\nDigite o texto cifrado com até 128 caracteres: "
                )
                plain = vigenere_decrypt(ciphertext, key)

                print("\nResultado")
                print("Cifrado  :", ciphertext)
                print("Decifrado:", plain)

        except Exception as error:
            print(f"\nErro: {error}")


if __name__ == "__main__":
    main()
