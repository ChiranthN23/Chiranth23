import pandas as pd
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset

# Load the dataset (update path if needed)
df = pd.read_csv("C:/Users/cn230/Chiranth/Chiranth23/adverse_drug_events_train.csv")


def preprocess_data(df):
    # Ensure the dataset has 'text' and 'label' columns
    df = df.rename(columns={"input": "text", "output": "label"})
    df = df.dropna()
    
    # Convert labels to numeric (ADR = 1, Non-ADR = 0)
    df["label"] = df["label"].apply(lambda x: 1 if x == "adverse drug event" else 0)
    
    return df

df = preprocess_data(df)

# Convert to Hugging Face dataset
dataset = Dataset.from_pandas(df)

# Load BioBERT model and tokenizer
model_name = "dmis-lab/biobert-base-cased-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Split dataset for training and testing (80-20 split)
train_test_split = tokenized_datasets.train_test_split(test_size=0.2)
train_dataset = train_test_split["train"]
test_dataset = train_test_split["test"]

# Load model
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Fine-tune the model
trainer.train()

# Save the trained model
model.save_pretrained("./finetuned_adr_model")
tokenizer.save_pretrained("./finetuned_adr_model")

print("✅ Fine-tuning complete! Model saved.")