# irn_2015_acb8a8

IranMO | Iran | 2015 | Second Round | 1

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [irn_2015_acb8a8](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_acb8a8.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Iran

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

The answer is $99$. First consider the initial condition that all of eggs are in just one of boxes. In each step, we can transfer eggs to at most one new box and so we need at least $99$ steps. We claim that $99$ steps is always enough. For this end, we call a box containing exactly $30$ eggs and $10$ kilograms of rice a *good box*, and a box which is not good a *bad box*! In each step, consider one of bad boxes containing the most number of eggs and one of bad boxes containing the most amount of rice. If these two boxes were the same, consider another arbitrary bad box (note that if all other boxes were good, this box also must be good and there is nothing to prove). Evidently, we have at least $30$ number of eggs and $10$ kilograms of rice in these two boxes. So by transferring eggs and rice between them, we can make one of them a good box. Therefore, after $99$ steps we have at least $99$ good boxes and so the last box is also good and we are done.

