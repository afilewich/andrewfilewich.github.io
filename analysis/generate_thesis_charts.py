from pathlib import Path
import csv
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "assets" / "data"
IMG_DIR = ROOT / "assets" / "img" / "thesis"
IMG_DIR.mkdir(parents=True, exist_ok=True)


def read_video_viewership():
    path = DATA_DIR / "video_viewership.csv"
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                "lab": row["lab"],
                "topic": row["topic"],
                "unique_views": int(row["unique_views"]),
                "enrollment": int(row["enrollment"]),
                "percent_of_class": float(row["percent_of_class"]),
            })
    return rows


def read_category_means():
    path = DATA_DIR / "category_means.csv"
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                "category": row["category"],
                "mean_score": float(row["mean_score"]),
            })
    return rows


def make_viewership_chart(rows):
    labels = [f"Lab {row['lab']}" for row in rows]
    values = [row["unique_views"] for row in rows]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values)
    plt.title("Verified Unique Views Across Pre-Laboratory Video Modules")
    plt.xlabel("Video module")
    plt.ylabel("Unique views")
    plt.ylim(0, max(values) + 8)

    for bar, row in zip(bars, rows):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f"{row['unique_views']} ({row['percent_of_class']}%)",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    plt.savefig(IMG_DIR / "video_viewership_chart.png", dpi=300, bbox_inches="tight")
    plt.close()


def make_category_means_chart(rows):
    labels = [row["category"] for row in rows]
    values = [row["mean_score"] for row in rows]

    plt.figure(figsize=(9, 5))
    bars = plt.bar(labels, values)
    plt.title("Descriptive Mean Scores by Category")
    plt.xlabel("Category")
    plt.ylabel("Mean score")
    plt.ylim(0, 5)
    plt.xticks(rotation=20)

    for bar, value in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.05,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    plt.savefig(IMG_DIR / "category_means_chart.png", dpi=300, bbox_inches="tight")
    plt.close()


def main():
    video_rows = read_video_viewership()
    category_rows = read_category_means()

    make_viewership_chart(video_rows)
    make_category_means_chart(category_rows)

    print("Charts generated in assets/img/thesis/")


if __name__ == "__main__":
    main()
