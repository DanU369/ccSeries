ALTER TABLE IF EXISTS ONLY public.episodes DROP CONSTRAINT IF EXISTS fk_episodes_season_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.seasons DROP CONSTRAINT IF EXISTS fk_seasons_show_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.show_characters DROP CONSTRAINT IF EXISTS fk_show_characters_show_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.show_characters DROP CONSTRAINT IF EXISTS fk_show_characters_actor_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.show_genres DROP CONSTRAINT IF EXISTS fk_show_genres_genre_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.show_genres DROP CONSTRAINT IF EXISTS fk_show_genres_show_id CASCADE;


ALTER TABLE public.episodes ADD CONSTRAINT fk_episodes_season_id FOREIGN KEY (season_id) REFERENCES seasons(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.seasons ADD CONSTRAINT fk_seasons_show_id FOREIGN KEY (show_id) REFERENCES shows(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.show_characters ADD CONSTRAINT fk_show_characters_show_id FOREIGN KEY (show_id) REFERENCES shows(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.show_characters ADD CONSTRAINT fk_show_characters_actor_id FOREIGN KEY (actor_id) REFERENCES actors(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.show_genres ADD CONSTRAINT fk_show_genres_genre_id FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.show_genres ADD CONSTRAINT fk_show_genres_show_id FOREIGN KEY (show_id) REFERENCES shows(id) ON DELETE CASCADE ON UPDATE CASCADE;
