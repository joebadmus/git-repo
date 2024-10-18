import time


def wait_until(predicate, assertion_failure_message, wait_seconds=0.5, max_retries=10):
    """Waits until a given condition becomes true, with retries and timeouts.

    Args:
      predicate: A callable that returns True when the condition is met.
      assertion_failure_message: A message to raise if the condition is not met
        after retries.
      wait_seconds: The number of seconds to wait between retries (default: 0.5).
      max_retries: The maximum number of retries before raising an exception (default: 10).

    Raises:
      AssertionError: If the condition is not met after the specified number of retries.
    """

    for _ in range(max_retries):
        if predicate():
            return

        time.sleep(wait_seconds)

    raise AssertionError(assertion_failure_message)


def wait_no_assertion_failure(assertion_action, wait_seconds=0.5, max_retries=10):
    """Waits until a given action can be executed without raising an assertion error,
    with retries and timeouts.

    Args:
      assertion_action: A callable that may raise an AssertionError.
      wait_seconds: The number of seconds to wait between retries (default: 0.5).
      max_retries: The maximum number of retries before raising an exception (default: 10).

    Raises:
      AssertionError: If the action raises an AssertionError after the specified number
        of retries.
    """

    for _ in range(max_retries):
        try:
            assertion_action()
            return
        except AssertionError:
            if _ == max_retries - 1:
                raise

        time.sleep(wait_seconds)

    # More informative message
    raise AssertionError("Assertion error occurred after retries")
