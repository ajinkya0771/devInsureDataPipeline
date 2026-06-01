import os
import pandas as pd


CURATED_FOLDER = "data/curated"
SEMANTIC_FOLDER = "data/semantic"


def build_curated_and_semantic(preprocessed_dataframes):

    print("Transformation layer started")

    # Load dataframes
    claims_df = preprocessed_dataframes["claims_20251017.csv"]

    payments_df = preprocessed_dataframes["payments_20251017.csv"]

    customers_df = preprocessed_dataframes["customers_20251017.csv"]

    policies_df = preprocessed_dataframes["policies_20251017.csv"]

    # CURATED LAYER
    curated_claims = claims_df.copy()

    curated_claims["load_status"] = "CURATED"

    curated_output_path = os.path.join(
        CURATED_FOLDER,
        "claims_enriched.parquet"
    )

    curated_claims.to_parquet(
        curated_output_path,
        index=False
    )

    print(f"Curated layer created → {curated_output_path}")

    # SEMANTIC LAYER
    semantic_df = claims_df.groupby(
        "policy_id"
    )["claim_amount"].sum().reset_index()

    semantic_df.rename(
        columns={
            "claim_amount": "total_claim_amount"
        },
        inplace=True
    )

    semantic_output_path = os.path.join(
        SEMANTIC_FOLDER,
        "policies_total_claimAmt.parquet"
    )

    semantic_df.to_parquet(
        semantic_output_path,
        index=False
    )

    print(f"Semantic layer created → {semantic_output_path}")

    return {
        "curated": curated_claims,
        "semantic": semantic_df
    }
