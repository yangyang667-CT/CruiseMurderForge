from pathlib import Path
import sys

project = Path(sys.argv[1] if len(sys.argv) > 1 else "extracted/CruiseMurderForge")
java = project / "src/main/java"

def replace_exact(relative, old, new, expected=1):
    path = java / relative
    text = path.read_text(encoding="utf-8")
    found = text.count(old)
    if found != expected:
        raise SystemExit(f"{path}: expected {expected} occurrence(s), found {found} for {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")

replace_exact(
    "com/cruisemurder/network/ModNetwork.java",
    "import net.minecraftforge.network.SimpleChannel;",
    "import net.minecraftforge.network.simple.SimpleChannel;"
)
replace_exact(
    "com/cruisemurder/CruiseMurderMod.java",
    "import net.minecraft.commands.arguments.StringArgumentType;",
    "import com.mojang.brigadier.arguments.StringArgumentType;"
)
replace_exact(
    "com/cruisemurder/client/HallucinationRenderEvents.java",
    "import net.minecraft.client.player.AbstractClientPlayer;",
    "import net.minecraft.world.entity.player.Player;"
)
replace_exact(
    "com/cruisemurder/client/HallucinationRenderEvents.java",
    "AbstractClientPlayer player = event.getEntity();",
    "Player player = event.getEntity();",
    expected=2
)
print("Applied 1.20.1 Forge source compatibility fixes.")
