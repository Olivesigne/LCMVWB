import os
import time
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
token = "MTI3NjE0MzYwNjUzNjg2Mzc4Ng.Gnz4wy.YA49Q92yWNOJcxcYESFvGNka119-BapovPmYFU"
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Bonjour ! {ctx.author}")

@bot.command()
async def list(ctx):
    await ctx.send("Liste des commandes : \n- !bonjour \n  - Le bot te dit bonjour \n \n- !list \n  - La liste des commandes \n \n- !info \n  - Ping tout le monde \n \n- !graphistes \n  - Ping les graphistes \n \n- !devs \n  - Ping les développeurs \n \n- !goat \n  - Ping le goat (Ne pas abuser) \n \n- !idee \n  - Ping tout le mode et les gens doivent réagir \n \n- !invite nom métier  \n  - Demande aux gens si la personne peut inviter quelqu'un \n- !reseaux \n - Affiche les réseaux du jeu")

@bot.command()
async def info(ctx):
    await ctx.send("@everyone Tout le monde :point_up: !")

@bot.command()
async def graphistes(ctx):
    await ctx.send("<@&1276277931714412557> :point_up: !")

@bot.command()
async def devs(ctx):
    await ctx.send("<@&1276277118250254378> :point_up: !")

@bot.command()
async def goat(ctx):
    await ctx.send("<@&1276276439892889651> :point_up: !")

@bot.command()
async def idee(ctx):
    await ctx.send("@everyone ✔ ou ❌ :point_up: ! Réagissez !")

@bot.command()
async def invite(ctx):
    await ctx.send("@everyone :point_up: ! Peut-on l'inviter ?")

@bot.command()
async def compterendu(ctx):
    await ctx.send("||@here|| \nCompte rendu du 23/08/24 : \n - Lundi réunion 11h \n - Fusillades \n - Accidents de voitures \n - Univers gratuit \n - Bateaux \n - Fusées \n - Métiers: \n	Banquiers \n	Pompiers \n	Policiers \n	Militaire \n	Artificiers \n	Agriculteurs \n	DJ \n - Iles \n - Evènement JO 2028: \n	Surf \n	Escrime \n	Football \n	Athlétisme \n	Cérémonie d'ouverture et de clotûre \n - Illerio graphisme [Free] : 'https://discord.gg/graph' \n  - Vidéo chat gpt: \n	Je ne peux pas générer de vidéos directement, mais je peux t'aider à concevoir un script pour une bande-annonce vidéo de ton jeu de simulation de vie LifeCraft: My Virtual World. Voici une idée de script que tu pourrais utiliser : \n	 \n[Ouverture] \n	Scène : Un ciel bleu clair avec des nuages doux, transitionnant vers un monde virtuel vibrant. \n	Voix Off (douce et engageante): Bienvenue dans LifeCraft: My Virtual World, où chaque jour est une nouvelle aventure.	 \n[Scène 1] \n	Montrer un personnage personnalisé se réveillant dans une maison cosy. \n	Voix Off: Créez votre ropre avatar et personnalisez chaque détail de votre maison.	 \n[Scène 2] \n	Le personnage sort de la maison, saluant des voisins dans une communauté virtuelle animée.	Voix Off: Explorez un monde vivant, où chaque voisin est un nouvel ami.	 \n[Scène 3] \n	Plan rapproché sur le personnage travaillant, jardinant, et participant à diverses activités communautaires. \n	Voix Off: Vivez la vie que vous avez toujours rêvé, avec des milliers de possibilités à portée de main.	 \n[Scène 4] \n	Montrer des scènes de construction, avec des maisons et des jardins prenant vie sous les mains du joueur. \n	Voix Off: Bâtissez, créez, et faites grandir votre monde, un bloc à la fois. \n	 \n[Scène 5] \n	Transition vers une scène de célébration avec des feux d'artifice et des personnages dansant ensemble. \n	Voix Off: Rejoignez une communauté mondiale, où chaque décision compte et chaque moment est spécial. \n \n")
    await ctx.send("        \n[Clôture] \n	Affichage du logo LifeCraft: My Virtual World avec un fond coloré et énergique. \n	Voix Off: Téléchargez LifeCraft: My Virtual World aujourd hui, et commencez votre nouvelle vie virtuelle. \n||@here||")

@bot.command()
async def reseaux(ctx):
    await ctx.send("Les réseaux du jeu : https://bit.ly/m/Life-Craft-My-Virtual-World \n Allez y faire un tour ! 😉")

@bot.command()
async def ok(ctx):
    await ctx.send("Le bot est en marche !")

#L'erreur est sur les 6 prochaines lignes
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1276278528845021185)
    member = await bot.get_user_info("User's ID here")
    await bot.send_message(member, f"Salut {discord.Member.mention}, bienvenue sur le serveur du jeu \"Life Craft : My Virtual World\" ! \nOn espère que le serveur te plaira ! 😉 \nBonne visite {discord.Member.name} !")
    await channel.send(f"Bienvenue a {discord.Member.mention} sur le serveur ! 😁")

bot.run(token)