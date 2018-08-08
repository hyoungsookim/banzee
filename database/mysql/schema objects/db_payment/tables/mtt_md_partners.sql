/*
    Partners
*/
create table mtt_md_partners
(
    partner_id          varchar(50)         not null,
    partner_status      smallint            not null,
    partner_name        varchar(50)         not null,
    created_at          datetime            not null,
    updated_at          datetime            not null,

    constraint pk_mtt_md_partners
        primary key (partner_id)
);
