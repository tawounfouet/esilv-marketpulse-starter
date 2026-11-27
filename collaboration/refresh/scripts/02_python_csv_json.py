#!/usr/bin/env python3
"""TD02 - Dictionnaires JSON, lignes CSV, filtres et fonctions réutilisables.

Ce script lit les mêmes fichiers que MarketPulse, sans les modifier.
Modèle mental : DATA SOURCE -> PARSING -> VALIDATION -> BUSINESS LOGIC -> OUTPUT.
Il n'enseigne PAS encore rendement, base 100 ou performance relative (TD07).
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DATA = ROOT / "data" / "sample"
REQUIRED_FIELDS = {"date", "ticker", "open", "high", "low", "close", "volume"}


def load_instruments(data_dir: Path) -> dict:
    """JSON -> dict : un ensemble de métadonnées métier nommées."""
    with (data_dir / "instruments.json").open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("Le JSON doit contenir un dictionnaire principal.")
    for role in ("instrument", "benchmark"):
        if not isinstance(data.get(role), dict) or not data[role].get("ticker"):
            raise ValueError(f"Métadonnées manquantes : {role}.ticker")
    return data


def load_prices(data_dir: Path) -> list[dict[str, str]]:
    """CSV -> liste de dictionnaires. Attention : les cellules restent du texte."""
    with (data_dir / "prices.csv").open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not REQUIRED_FIELDS.issubset(set(reader.fieldnames or [])):
            raise ValueError(f"Colonnes manquantes : {REQUIRED_FIELDS - set(reader.fieldnames or [])}")
        return list(reader)


def filter_prices(prices: list[dict[str, str]], ticker: str) -> list[dict[str, str]]:
    """Même fonction, deux instruments : la réutilisation évite la duplication."""
    return [row for row in prices if row["ticker"] == ticker]


def first_last_close(prices: list[dict[str, str]]) -> tuple[float, float]:
    """La conversion explicite empêche de confondre nombre et chaîne."""
    if not prices:
        raise ValueError("Série vide : impossible d'obtenir les cours.")
    sorted_prices = sorted(prices, key=lambda row: row["date"])
    return float(sorted_prices[0]["close"]), float(sorted_prices[-1]["close"])


def display_summary(asset: dict, prices: list[dict[str, str]]) -> None:
    """Une seule logique de synthèse pour l'instrument et le benchmark."""
    first, last = first_last_close(prices)
    ticker = asset["ticker"]
    print(f"\n{ticker} - {asset['name']}")
    print(f"  Observations : {len(prices)}")
    print(f"  Premier close : {first:.2f}")
    print(f"  Dernier close : {last:.2f}")


def main() -> int:
    parser = argparse.ArgumentParser(description="TD02 : explorer JSON et CSV sans écriture.")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA, help="Dossier contenant instruments.json et prices.csv")
    args = parser.parse_args()
    data_dir: Path = args.data_dir

    # Les chemins et contrats de données sont aussi importants que le code.
    instruments = load_instruments(data_dir)
    prices = load_prices(data_dir)
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    print("=== TD02 : DONNÉES DE MARCHÉ ===")
    print(f"Type du JSON : {type(instruments).__name__}")
    print(f"Type du CSV : {type(prices).__name__}[{type(prices[0]).__name__}]" if prices else "CSV vide")
    if prices:
        print(f"Type du champ close lu : {type(prices[0]['close']).__name__} -> après float : float")

    for asset in (instrument, benchmark):
        display_summary(asset, filter_prices(prices, asset["ticker"]))

    # Ce nombre vient du jeu d'exemple officiel. Ne pas supposer que toutes
    # les sources de marché auront toujours 21 observations.
    print("\nJeu pédagogique attendu : 21 observations pour AAPL et 21 pour SP500.")
    print("Rappel professionnel : valider types, schéma et période AVANT l'analyse.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
