import re

# Caminho do appinfo.vdf
caminho = r"D:\Steam\appcache\appinfo.vdf"

# Arquivos de saída
saida_ids = r"C:\Users\Daniel\Documents\PC- Notas\manifests.txt"
saida_cmds = r"C:\Users\Daniel\Documents\PC- Notas\comandos_steamcmd.txt"

# AppID e DepotID que você quer
app_id = "65800"
depot_id = "65801"

# Ler arquivo
with open(caminho, "rb") as f:
    data = f.read()

text = data.decode(errors="ignore")

# Encontrar todos os números de 18 a 20 dígitos (possíveis ManifestIDs)
candidatos = re.findall(r'\d{18,20}', text)
candidatos = list(set(candidatos))  # remover duplicatas

print(f"Encontrados {len(candidatos)} possíveis ManifestIDs.")

# Salvar todos os ManifestIDs em um arquivo
with open(saida_ids, "w") as f_out:
    for c in candidatos:
        f_out.write(c + "\n")

print(f"Todos os ManifestIDs foram salvos em: {saida_ids}")

# Gerar comandos SteamCMD para o DepotID escolhido
with open(saida_cmds, "w") as f_cmd:
    for gid in candidatos:
        f_cmd.write(f"download_depot {app_id} {depot_id} {gid}\n")

print(f"Comandos SteamCMD gerados em: {saida_cmds}")
