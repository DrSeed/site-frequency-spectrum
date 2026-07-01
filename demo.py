import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(3);n=100;S=5000
# neutral SFS ~ 1/i
i=np.arange(1,n)
prob=(1/i);prob/=prob.sum()
counts=rng.multinomial(S,prob)
plt.figure(figsize=(8,4));plt.bar(i,counts,color="teal")
plt.xlabel("derived allele count");plt.ylabel("number of sites");plt.title("Site frequency spectrum (demo data)")
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"{S} segregating sites\n");print("ok")