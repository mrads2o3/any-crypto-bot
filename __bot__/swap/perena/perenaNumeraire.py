from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey # type: ignore
from solana.transaction import Transaction
from solders.keypair import Keypair # type: ignore
from solana.rpc.types import TxOpts
from anchorpy import Program, Context, Idl
import base64
import asyncio

# Konstanta
PROGRAM_ID = Pubkey.from_string("NUMERUNsFCP3kuNmWZuXtm1AaQCPj9uw6Guv2Ekoi5P")
TOKEN_PROGRAM_ID = Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")
TOKEN_2022_PROGRAM_ID = Pubkey.from_string("TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb")
USDC_MINT = Pubkey.from_string("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")
USDC_TRADER = Pubkey.from_string("FGGeaaqcCbWZ1eNT11KS8rU9JGhu7Nh8pLaozh4HEWrK")
USDC_VAULT = Pubkey.from_string("6B8k8At9879r5EsZAWg8W6DEpxzJ798Cwj48twu3pq4b")
USDT_MINT = Pubkey.from_string("Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB")
USDT_TRADER = Pubkey.from_string("6bFsv7He5NEECj6SZCXV2q7146mUWbRyAb7P4zMFMnAq")
USDT_VAULT = Pubkey.from_string("DJfYbGicp4AFXWsragNWv1baugqcdFhw6eFTcK2YWdyK")
POOL = Pubkey.from_string("2w4A1eGyjRutakyFdmVyBiLPf98qKxNTC2LpuwhaCruZ")
NUMERAIRE_CONFIG = Pubkey.from_string("FS159v4b2jo3fjGBaUFmDzgx7k616XhpKhMwX2Q3HeeD")
PAYER = Pubkey.from_string("PUBLIC_KEY")

async def swap_tokens(client, payer, pool, in_mint, out_mint, in_trader, out_trader, in_vault, out_vault, amount):
    # Load the IDL
    with open("idl_numeraire.json", "r") as f:
        idl_data = f.read()
    idl = Idl.from_json(idl_data)

    # Load the program
    program = Program(idl, PROGRAM_ID, client)

    # Buat instruksi swap
    tx = await program.rpc["swap_exact_in"](
        {"amount": amount},  # Isi data sesuai dengan IDL
        ctx=Context(
            accounts={
                "pool": POOL,
                "in_mint": in_mint,
                "out_mint": out_mint,
                "in_trader": in_trader,
                "out_trader": out_trader,
                "in_vault": in_vault,
                "out_vault": out_vault,
                "numeraire_config": NUMERAIRE_CONFIG,
                "payer": PAYER,
                "token_program": TOKEN_PROGRAM_ID,
                "token_2022_program": TOKEN_2022_PROGRAM_ID,
            },
            signers=[payer],
        ),
    )
    print("Transaction sent:", tx)

# Main function
async def perenaNumeraire(PrivateKey):
    client = AsyncClient("https://api.mainnet-beta.solana.com")
    payer = "Keypair.from_base58_string(PrivateKey)"
    pool = POOL
    
    # Logic menentukan in/out mint
    in_mint = USDT_MINT  # Contoh Anda memiliki USDT
    in_trader = USDT_TRADER
    in_vault = USDT_VAULT
    out_mint = USDC_MINT
    out_trader = USDC_TRADER
    out_vault = USDC_VAULT
    
    # Swap semua token di akun in_trader
    amount = 100000000  # Contoh, jumlah token dalam smallest unit
    await swap_tokens(client, payer, pool, in_mint, out_mint, in_trader, out_trader, in_vault, out_vault, amount)
    await client.close()

# Run
asyncio.run(perenaNumeraire("PrivateKey"))
