import json
import sqlite3


def main():
    database = sqlite3.connect(":memory:")
    database.executescript(
        """
        CREATE TABLE sessions (session_id TEXT, repo TEXT, adopted_lines INTEGER);
        CREATE TABLE commits (commit_id TEXT, repo TEXT);
        CREATE TABLE changes (change_id TEXT, repo TEXT);
        CREATE TABLE workitems (workitem_id TEXT, related_change_id TEXT);
        INSERT INTO sessions VALUES ('session-1', 'project', 10), ('session-2', 'project', 20);
        INSERT INTO commits VALUES ('commit-1', 'project'), ('commit-2', 'project'), ('commit-3', 'project');
        INSERT INTO changes VALUES ('change-1', 'project'), ('change-2', 'project');
        INSERT INTO workitems VALUES ('workitem-1', 'change-1'), ('workitem-2', 'change-2');
        """
    )
    source_totals = database.execute(
        "SELECT count(session_id), sum(adopted_lines) FROM sessions"
    ).fetchone()
    repo_join_totals = database.execute(
        """
        SELECT count(session_id), sum(adopted_lines)
        FROM sessions
        JOIN commits USING (repo)
        JOIN changes USING (repo)
        JOIN workitems ON workitems.related_change_id = changes.change_id
        """
    ).fetchone()
    aggregated_totals = database.execute(
        """
        WITH session_totals AS (
            SELECT repo, count(session_id) AS session_count, sum(adopted_lines) AS adopted_lines
            FROM sessions GROUP BY repo
        ), commit_totals AS (
            SELECT repo, count(commit_id) AS commit_count FROM commits GROUP BY repo
        ), change_totals AS (
            SELECT repo, count(change_id) AS change_count FROM changes GROUP BY repo
        )
        SELECT session_count, adopted_lines
        FROM session_totals
        JOIN commit_totals USING (repo)
        JOIN change_totals USING (repo)
        """
    ).fetchone()
    assert source_totals == (2, 30), source_totals
    assert repo_join_totals == (12, 180), repo_join_totals
    assert aggregated_totals == source_totals, aggregated_totals
    database.close()
    print(
        json.dumps(
            {
                "scope": "synthetic counterexample to a repo-only measurement join; not an agent eval",
                "source_totals": {"sessions": source_totals[0], "adopted_lines": source_totals[1]},
                "repo_join_totals": {"sessions": repo_join_totals[0], "adopted_lines": repo_join_totals[1]},
                "aggregated_totals": {"sessions": aggregated_totals[0], "adopted_lines": aggregated_totals[1]},
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
