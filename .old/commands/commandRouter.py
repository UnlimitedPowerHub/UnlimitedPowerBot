from telegram import Update
from telegram.ext import ContextTypes

class CommandRouter:
    def __init__(self, prefix="."):
        self.prefix = prefix
        self.routes = {}

    def add(self, path, func):
        self.routes[path] = func

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        
        if not update.message:
            return
        text = update.message.text.strip()
        if not text.startswith(self.prefix):
            return
        if text == ".":
            return
    
        cmd_text = text[len(self.prefix):].lstrip(".")
        parts = cmd_text.split()
        command = parts[0]
        args = parts[1:]

        keys = sorted(self.routes.keys(), key=lambda x: -len(x))
        for k in keys:
            if command == k or command.startswith(k + "."):
                sub = command[len(k):].strip(".")
                if sub:
                    args = [sub] + args
                await self.routes[k](update, context, args)
                return
