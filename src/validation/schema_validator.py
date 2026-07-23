from src.utils.logger import logger


def validate_columns(df, required_columns):
    actual = set(df.columns)
    required = set(required_columns)

    missing = required - actual

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    logger.info("Schema validation passed")