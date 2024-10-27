import subprocess

def load_model():
    # Run command in terminal to load the model
    options = ["--num_chunks 16", "--run_name MMULA_evaluate", "--max_epochs 20", "--num_heads_labattn 1", "--patience_threshold 3",
        "--debug False", "--evaluate_temporal True", "--use_multihead_attention True", "--weight_aux 0", "--num_layers 1", 
        "--num_attention_heads 1", "--setup random", "--limit_ds 0", "--is_baseline False", "--aux_task none", 
        "--use_all_tokens False", "--apply_transformation False", "--apply_weight False", "--reduce_computation True", 
        "--apply_temporal_loss False", "--save_model True"]
    subprocess.run(["python", "model/main.py"] + options)
    # return weights