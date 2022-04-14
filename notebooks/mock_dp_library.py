import numpy as np
np.random.seed(1234)


def laplace(shift=0., scale=1., size=None):
    """Sample from the laplace distribution."""
    p = np.random.uniform(low=-0.5, high=0.5, size=size)
    draws = shift - scale * np.sign(p) * np.log(1 - 2 * abs(p))
    return draws

    # the easy way
    # return np.random.laplace(loc=shift, scale=scale, size=size)


def gaussian(shift=0., scale=1., size=None):
    """Sample from the Gaussian distribution."""
    draws = np.random.normal(loc=shift, scale=scale, size=size)
    return draws


def bernoulli(p, size=None):
    return np.random.uniform(size=size) < p


def discrete_laplace(loc, scale):
    if not scale:
        return loc
    alpha = np.exp(-1 / scale)

    noise = 0 if bernoulli(p=(1 - alpha) / (1 + alpha)) else np.random.geometric(1 - alpha)
    if bernoulli(p=0.5):
        noise *= -1
    return loc + noise


def cond_laplace(shift, scale):
    """Conditionally sample from laplace or discrete laplace depending on the dtype of `shift`"""
    if np.issubdtype(type(shift), np.integer):
        return discrete_laplace(shift, scale)
    if np.issubdtype(type(shift), np.float):
        return np.random.laplace(shift, scale)
    else:
        raise ValueError(f"unrecognized type {type(low)}")
    

def cond_uniform(low, high):
    """Conditionally sample from discrete or continuous uniform based on the dtype of `low`"""
    if np.issubdtype(type(low), np.integer):
        return low if low == high else np.random.randint(low, high)
    if np.issubdtype(type(low), np.float):
        return np.random.uniform(low, high)
    else:
        raise ValueError(f"unrecognized type {type(low)}")


def clamp(x, bounds):
    """Replace any x_i less than lower with lower, 
           and any x_i greater than upper with upper."""
    return np.clip(x, *bounds)


def bounded_mean(x, bounds):
    x_clamped = clamp(x, bounds)
    return np.mean(x_clamped)


def release_dp_mean(x, bounds, epsilon, delta=1e-6, mechanism="laplace"):
    """Release a DP mean. 
    Assumes that the dataset size n is public information.
    """
    sensitive_mean = bounded_mean(x, bounds)

    n = len(x)
    lower, upper = bounds
    # Sensitivity in terms of an absolute distance metric
    # Both the laplace and gaussian mechanisms can noise queries
    #    with sensitivities expressed in absolute distances
    sensitivity = (upper - lower) / n
    
    if mechanism == "laplace":
        scale = sensitivity / epsilon
        dp_mean = sensitive_mean + laplace(scale=scale)
    elif mechanism == "gaussian":
        scale = (sensitivity / epsilon) * np.sqrt(2*np.log(2/delta)) 
        dp_mean = sensitive_mean + gaussian(scale=scale)
    else:
        raise ValueError(f"unrecognized mechanism: {mechanism}")

    return dp_mean

    # the compact way
    # return laplace(shift=mean(x_clamped(x)), scale=(upper-lower)/(n*epsilon))
    # return gaussian(shift=mean(x_clamped(x)), scale=(upper-lower)/(n*epsilon))
    

def bootstrap(x, n):
    """Sample n values with replacement from n."""
    index = np.random.randint(low=0., high=len(x), size=n)
    return x[index]


def release_dp_histogram(x, epsilon, categories):
    """Release an `epsilon`-DP estimate of the counts of each of the `categories`"""
    sensitivity = 2
    scale = sensitivity / epsilon

    # create a {category: count} hashmap
    counts = dict(zip(*np.unique(x, return_counts=True)))
    # look up the count of each category, or zero if not exists
    sensitive_histogram = np.array([counts.get(cat, 0) for cat in categories])

    dp_histogram = sensitive_histogram + laplace(scale=scale, size=sensitive_histogram.shape)
    return dp_histogram
